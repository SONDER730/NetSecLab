<template>
  <div class="main-container">
    <!-- 左侧菜单 -->
    <el-menu
      class="el-menu-vertical"
      :default-active="activeMenu"
      @select="handleMenuSelect"
      background-color="#001f3f"
      text-color="#fff"
      active-text-color="#409eff"
    >
      <el-menu-item index="teacherInfo">
        教师信息
      </el-menu-item>
      <el-menu-item index="studentManagement">
        学生管理
      </el-menu-item>
      <el-menu-item index="competitionManagement">
        竞赛管理
      </el-menu-item>
      <!--
      <el-menu-item index="reportCertificates">
        报告与证书
      </el-menu-item>
      -->
      <el-menu-item index="generatePDF">
        生成PDF证明
      </el-menu-item>
    </el-menu>

    <!-- 右侧内容展示 -->
    <div class="content-container">
      <!-- 教师信息模块 -->
      <div v-if="activeMenu === 'teacherInfo'">
        <div class="info-notification">
          <el-card>
            <p>待审核学生竞赛申请: {{ pendingStudents }}</p>
            <p>未完成竞赛流程: {{ pendingCompetitions }}</p>
            <p>系统通知: {{ systemNotifications }}</p>
          </el-card>
        </div>
        <div class="teacher-info">
          <h2>教师个人信息</h2>
          <el-card>
            <el-descriptions column="1" border>
              <el-descriptions-item label="姓名">{{ teacherInfo.name }}</el-descriptions-item>
              <el-descriptions-item label="学院">{{ teacherInfo.department }}</el-descriptions-item>
              <el-descriptions-item label="职位">{{ teacherInfo.position }}</el-descriptions-item>
              <el-descriptions-item label="工号">{{ teacherInfo.id }}</el-descriptions-item>
              <el-descriptions-item label="联系方式">{{ teacherInfo.phone }}</el-descriptions-item>
              <el-descriptions-item label="邮箱">{{ teacherInfo.email }}</el-descriptions-item>
            </el-descriptions>
          </el-card>
        </div>
      </div>

      <!-- 学生管理模块 -->
      <div v-if="activeMenu === 'studentManagement'">
        <h2>学生管理</h2>
        <el-input v-model="searchQuery" placeholder="按学生姓名、学号、竞赛项目进行搜索"></el-input>
        <el-table :data="studentData" stripe>
          <el-table-column prop="name" label="姓名"></el-table-column>
          <el-table-column prop="studentID" label="学号"></el-table-column>
          <el-table-column prop="competition" label="竞赛项目"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="small" @click="approveStudent(scope.row)">批准</el-button>
              <el-button size="small" type="danger" @click="rejectStudent(scope.row)">拒绝</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <!-- 竞赛管理模块 -->
      <div v-if="activeMenu === 'competitionManagement'">
        <h2>竞赛管理</h2>
        <el-table :data="competitionData" stripe>
          <el-table-column prop="name" label="竞赛名称"></el-table-column>
          <el-table-column prop="id" label="编号"></el-table-column>
          <el-table-column prop="status" label="流程状态"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="small" @click="reviewMaterials(scope.row)">查看材料</el-button>
              <el-button size="small" @click="confirmProcess(scope.row)">确认流程</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <!-- 报告与证书模块 -->
      <!--
      <div v-if="activeMenu === 'reportCertificates'">
        <h2>报告与证书</h2>
        <el-input v-model="searchQuery" placeholder="按学生、竞赛项目、时间进行搜索"></el-input>
        <el-table :data="reportData" stripe>
          <el-table-column prop="studentName" label="学生姓名"></el-table-column>
          <el-table-column prop="competition" label="竞赛项目"></el-table-column>
          <el-table-column prop="uploadDate" label="上传日期"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="small" @click="viewReport(scope.row)">查看总结</el-button>
              <el-button size="small" @click="viewCertificate(scope.row)">查看证书</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
      -->

      <!-- 生成PDF证明模块 -->
      <div v-if="activeMenu === 'generatePDF'">
        <h2>生成PDF证明</h2>
        <el-table :data="pdfData" stripe>
          <el-table-column prop="studentName" label="学生姓名"></el-table-column>
          <el-table-column prop="competition" label="竞赛项目"></el-table-column>
          <el-table-column prop="status" label="状态"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="small" type="success" @click="generatePDF(scope.row)">生成PDF</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // 当前活动的 tab，默认是教师信息
      activeMenu: 'teacherInfo',

      // 通知数量
      pendingStudents: 5,
      pendingCompetitions: 3,
      systemNotifications: 2,

      // 教师信息
      teacherInfo: {
        name: '张老师',
        department: '计算机科学学院',
        position: '副教授',
        id: 'T123456',
        phone: '12345678901',
        email: 'teacher@example.com'
      },

      // 学生管理数据
      studentData: [
        { name: '张三', studentID: 'S123456', competition: '编程大赛' },
        { name: '李四', studentID: 'S234567', competition: 'AI挑战赛' }
      ],

      // 竞赛管理数据
      competitionData: [
        { name: '编程大赛', id: 'C001', status: '未完成' },
        { name: 'AI挑战赛', id: 'C002', status: '待确认' }
      ],

      // 报告与证书数据
      reportData: [
        { studentName: '张三', competition: '编程大赛', uploadDate: '2024-09-15' },
        { studentName: '李四', competition: 'AI挑战赛', uploadDate: '2024-09-16' }
      ],

      // 生成PDF证明数据
      pdfData: [
        { studentName: '张三', competition: '编程大赛', status: '未生成' },
        { studentName: '李四', competition: 'AI挑战赛', status: '已生成' }
      ],

      // 搜索查询
      searchQuery: ''
    };
  },
  methods: {
    handleMenuSelect(index) {
      this.activeMenu = index;
    },
    approveStudent(student) {
      console.log('批准学生:', student.name);
    },
    rejectStudent(student) {
      console.log('拒绝学生:', student.name);
    },
    reviewMaterials(competition) {
      console.log('查看材料:', competition.name);
    },
    confirmProcess(competition) {
      console.log('确认流程:', competition.name);
    },
    viewReport(student) {
      console.log('查看总结:', student.studentName);
    },
    viewCertificate(student) {
      console.log('查看证书:', student.studentName);
    },
    generatePDF(student) {
      console.log('生成PDF:', student.studentName);
    }
  }
};
</script>

<style scoped>
.main-container {
  display: flex;
  height: 100vh;
  background-color: #001f3f;
}

.el-menu-vertical {
  width: 250px;
  background-color: #001f3f;
  color: #fff;
}

.content-container {
  flex: 1;
  padding: 20px;
  background-color: white;
  color: black;
}

.el-menu-item {
  color: #fff !important;
}

.el-menu-item:hover {
  background-color: #409eff !important;
}

.el-menu-item.is-active {
  background-color: #409eff !important;
}

.info-notification {
  margin-bottom: 20px;
}

.teacher-info {
  margin-top: 20px;
}

.el-button {
  margin-left: 10px;
}
</style>
