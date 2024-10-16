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
      <el-menu-item index="reportCertificates">
        报告与证书
      </el-menu-item>
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

        <div v-if="!editMode">
          <div class="teacher-info">
            <h2>教师个人信息</h2>
            <el-card>
              <el-descriptions column="1" border>
                <el-descriptions-item label="姓名">{{ teacherInfo.name }}</el-descriptions-item>
                <el-descriptions-item label="学院">{{ teacherInfo.department }}</el-descriptions-item>
                <el-descriptions-item label="工号">{{ teacherInfo.teacher_id }}</el-descriptions-item>
                <el-descriptions-item label="联系方式">{{ teacherInfo.contact }}</el-descriptions-item>
                <el-descriptions-item label="邮箱">{{ teacherInfo.email }}</el-descriptions-item>
              </el-descriptions>
            </el-card>
            <el-button type="primary" @click="editMode = true">修改信息</el-button>
          </div>
        </div>

        <div v-else>
          <h2>修改教师信息</h2>
          <el-form :model="teacherInfo" label-width="80px">
            <el-form-item label="姓名">
              <el-input v-model="teacherInfo.name"></el-input>
            </el-form-item>
            <el-form-item label="学院">
              <el-input v-model="teacherInfo.department"></el-input>
            </el-form-item>
            <el-form-item label="工号">
              <el-input v-model="teacherInfo.teacher_id" ></el-input>
            </el-form-item>
            <el-form-item label="联系方式">
              <el-input v-model="teacherInfo.contact"></el-input>
            </el-form-item>
            <el-form-item label="邮箱">
              <el-input v-model="teacherInfo.email"></el-input>
            </el-form-item>
            <el-button type="primary" @click="submitTeacherInfo">提交</el-button>
            <el-button @click="editMode = false">取消</el-button>
          </el-form>
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
import axios from 'axios'; // 引入 axios

export default {
  data() {
    return {
      // 当前活动的 tab，默认是教师信息
      activeMenu: 'teacherInfo',
      editMode: false,

      // 通知数量
      pendingStudents: 5,
      pendingCompetitions: 3,
      systemNotifications: 2,

      // 教师信息
      teacherInfo: {
        name: '',
        department: '',
        teacher_id: '',
        contact: '',
        email: ''
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
  created() {
    this.fetchTeacherInfo(); // 组件创建时获取学生信息
  },
  methods: {
    handleMenuSelect(index) {
      this.activeMenu = index;
    },

    // 获取教师信息
    fetchTeacherInfo() {
      axios.get('/api/teacher-info/')
        .then(response => {
          // 假设返回的数据是一个数组，取第一个学生的信息
          if (response.data.length > 0) {
            this.profileForm = response.data[0];
          }
        })
        .catch(error => {
          console.error('Error fetching teacher info:', error);
        });
    },

    submitTeacherInfo() {
    console.log('Submitting teacher info:', this.teacherInfo);
      axios.post('/api/teacher-info/', this.teacherInfo)  // 使用 POST 方法
    .then(response => {
      this.$message.success('信息提交成功');
      this.editMode = false;
      this.fetchTeacherInfo(); // 提交后重新获取数据以更新视图
    })
    .catch(error => {
      this.$message.error('提交失败: ' + (error.response?.data?.message || error.message));
    });
    },

    // 学生管理操作
    approveStudent(student) {
      this.$message.success(`已批准学生：${student.name}`);
    },
    rejectStudent(student) {
      this.$message.error(`已拒绝学生：${student.name}`);
    },

    // 竞赛管理操作
    reviewMaterials(competition) {
      this.$message.info(`查看竞赛材料：${competition.name}`);
    },
    confirmProcess(competition) {
      this.$message.success(`确认竞赛流程：${competition.name}`);
    },

    // 报告与证书操作
    viewReport(report) {
      this.$message.info(`查看总结：${report.studentName}的${report.competition}总结`);
    },
    viewCertificate(report) {
      this.$message.info(`查看证书：${report.studentName}的${report.competition}证书`);
    },

    // PDF生成操作
    generatePDF(pdf) {
      this.$message.success(`已生成PDF：${pdf.studentName}的${pdf.competition}证明`);
    }
  },
  mounted() {
    this.fetchTeacherInfo();
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

.el-form-item {
  margin-bottom: 15px;
}
</style>
