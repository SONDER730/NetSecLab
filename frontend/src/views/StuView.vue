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
      <el-menu-item index="personalInfo">个人信息</el-menu-item>
      <el-menu-item index="myCompetitions">我的竞赛</el-menu-item>
      <el-menu-item index="certificateDownload">证书下载</el-menu-item>
      <el-menu-item index="paymentOrders">缴费订单</el-menu-item>
      <el-menu-item index="changePassword">修改密码</el-menu-item>
    </el-menu>

    <!-- 右侧内容展示 -->
    <div class="content-container">
      <div v-if="activeMenu === 'personalInfo'">
        <h2>个人信息</h2>
        <div v-if="!editMode">
          <el-row :gutter="20" class="info-display">
            <el-col :span="12">
              <el-card>
                <el-descriptions column="Number('1')">
                  <el-descriptions-item label="姓名">{{ profileForm.name }}</el-descriptions-item>
                  <el-descriptions-item label="学院">{{ profileForm.school }}</el-descriptions-item>
                  <el-descriptions-item label="专业">{{ profileForm.major }}</el-descriptions-item>
                  <el-descriptions-item label="学号">{{ profileForm.student_id }}</el-descriptions-item>
                </el-descriptions>
              </el-card>
            </el-col>
            <el-col :span="12">
              <el-card>
                <el-descriptions column="1" border>
                  <el-descriptions-item label="年级">{{ profileForm.grade }}</el-descriptions-item>
                  <el-descriptions-item label="性别">{{ profileForm.gender === 'male' ? '男' : '女' }}</el-descriptions-item>
                  <el-descriptions-item label="电话">{{ profileForm.phone }}</el-descriptions-item>
                  <el-descriptions-item label="邮箱">{{ profileForm.email }}</el-descriptions-item>
                </el-descriptions>
              </el-card>
            </el-col>
          </el-row>
          <el-button type="primary" @click="editMode = true">修改信息</el-button>
        </div>

        <div v-else>
          <el-form :model="profileForm" label-width="80px">
            <el-row :gutter="20">
              <el-col :span="12">
                <el-form-item label="姓名">
                  <el-input v-model="profileForm.name"></el-input>
                </el-form-item>
                <el-form-item label="学院">
                  <el-input v-model="profileForm.school"></el-input>
                </el-form-item>
                <el-form-item label="专业">
                  <el-input v-model="profileForm.major"></el-input>
                </el-form-item>
                <el-form-item label="学号">
                  <el-input v-model="profileForm.student_id"></el-input>
                </el-form-item>
              </el-col>
              <el-col :span="12">
                <el-form-item label="年级">
                  <el-select v-model="profileForm.grade" placeholder="请选择年级">
                    <el-option label="大一" value="大一"></el-option>
                    <el-option label="大二" value="大二"></el-option>
                    <el-option label="大三" value="大三"></el-option>
                    <el-option label="大四" value="大四"></el-option>
                  </el-select>
                </el-form-item>
                <el-form-item label="性别">
                  <el-radio-group v-model="profileForm.gender">
                    <el-radio label="male">男</el-radio>
                    <el-radio label="female">女</el-radio>
                  </el-radio-group>
                </el-form-item>
                <el-form-item label="电话">
                  <el-input v-model="profileForm.phone"></el-input>
                </el-form-item>
                <el-form-item label="邮箱">
                  <el-input v-model="profileForm.email"></el-input>
                </el-form-item>
              </el-col>
            </el-row>
            <el-button type="primary" @click="submitProfile">提交</el-button>
            <el-button @click="editMode = false">取消</el-button>
          </el-form>
        </div>
      </div>

      <div v-if="activeMenu === 'myCompetitions'">
        <h2>我的竞赛</h2>
        <el-table :data="competitionData" style="width: 100%">
          <el-table-column prop="id" label="竞赛ID"></el-table-column>
          <el-table-column prop="name" label="竞赛名称"></el-table-column>
          <el-table-column prop="progress" label="进度">
            <template slot-scope="scope">
              <el-progress :percentage="scope.row.progress"></el-progress>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button @click="handleUpload(scope.row.id)">上传材料</el-button>
              <el-button @click="viewStatus(scope.row.id)">查看状态</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <div v-if="activeMenu === 'certificateDownload'">
        <h2>证书下载</h2>
        <el-table :data="certificateData" style="width: 100%">
          <el-table-column prop="id" label="证书ID"></el-table-column>
          <el-table-column prop="name" label="证书名称"></el-table-column>
          <el-table-column prop="issueDate" label="发放日期"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button @click="downloadCertificate(scope.row.id)">下载证书</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <div v-if="activeMenu === 'paymentOrders'">
        <h2>缴费订单</h2>
        <el-table :data="paymentOrdersData" style="width: 100%">
          <el-table-column prop="id" label="订单ID"></el-table-column>
          <el-table-column prop="name" label="竞赛名称"></el-table-column>
          <el-table-column prop="peopleCount" label="人数"></el-table-column>
          <el-table-column prop="price" label="价格"></el-table-column>
          <el-table-column prop="invoiceStatus" label="发票状态"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button @click="handleViewInvoice(scope.row.id)">查看发票</el-button>
              <el-button @click="handleReissueInvoice(scope.row.id)">重新开票</el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

      <div v-if="activeMenu === 'changePassword'">
        <h2>修改密码</h2>
        <el-form :model="passwordForm" label-width="120px">
          <el-form-item label="旧密码">
            <el-input type="password" v-model="passwordForm.oldPassword"></el-input>
          </el-form-item>
          <el-form-item label="新密码">
            <el-input type="password" v-model="passwordForm.newPassword"></el-input>
          </el-form-item>
          <el-form-item label="确认密码">
            <el-input type="password" v-model="passwordForm.confirmPassword"></el-input>
          </el-form-item>
          <el-button type="primary" @click="submitPasswordChange">提交</el-button>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'; // 导入 Axios
import Calendar from '@/components/Calendar.vue';

export default {
  components: {
    Calendar
  },
  data() {
    return {
      activeMenu: 'personalInfo',
      editMode: false,
      profileForm: {
        name: '',
        student_id: '',
        gender: 'male',
        phone: '',
        email: '',
        school: '',
        major: '',
        grade: ''
      },
      showCalendar: false,
      competitionData: [
        { id: '001', name: '网络安全竞赛', progress: 70 },
        { id: '002', name: '编程马拉松', progress: 50 },
        { id: '003', name: '数据挖掘比赛', progress: 90 },
      ],
      certificateData: [
        { id: '001', name: '编程大赛证书', issueDate: '2024-09-20' },
        { id: '002', name: 'AI挑战赛证书', issueDate: '2024-09-22' },
      ],
      paymentOrdersData: [
        { id: '001', invoiceStatus: '已开票', name: '竞赛1', peopleCount: 3, price: '¥3000' },
        { id: '002', invoiceStatus: '未开票', name: '竞赛2', peopleCount: 5, price: '¥5000' },
        { id: '003', invoiceStatus: '已开票', name: '竞赛3', peopleCount: 2, price: '¥2000' },
      ],
      passwordForm: {
        oldPassword: '',
        newPassword: '',
        confirmPassword: ''
      }
    };
  },
  created() {
    this.fetchStudentInfo(); // 组件创建时获取学生信息
  },
  methods: {
    fetchStudentInfo() {
      axios.get('/api/student-info/')
        .then(response => {
          // 假设返回的数据是一个数组，取第一个学生的信息
          if (response.data.length > 0) {
            this.profileForm = response.data[0];
          }
        })
        .catch(error => {
          console.error('获取学生信息失败:', error);
        });
    },
    handleMenuSelect(index) {
      this.activeMenu = index;
    },
    submitProfile() {
  axios.post('/api/student-info/', this.profileForm)
    .then(response => {
      this.$message.success('信息提交成功');
      this.editMode = false;
      this.fetchStudentInfo(); // 重新获取信息以更新视图
    })
    .catch(error => {
      // 检查错误对象并提取信息
      if (error.response) {
        // 请求已发出，服务器响应了状态码
        // 不是 2xx 的范围
        this.$message.error('提交失败: ' + error.response.data.message || error.response.statusText);
      } else if (error.request) {
        // 请求已发出，但没有收到响应
        this.$message.error('提交失败: 没有收到响应');
      } else {
        // 其他错误
        this.$message.error('提交失败: ' + error.message);
      }
    });

    },
    toggleCalendar() {
      this.showCalendar = !this.showCalendar;
    },
    handleUpload(competitionId) {
      console.log('上传材料', competitionId);
    },
    viewStatus(competitionId) {
      console.log('查看状态', competitionId);
    },
    handleViewInvoice(orderId) {
      console.log('查看发票', orderId);
    },
    handleReissueInvoice(orderId) {
      console.log('重新开票', orderId);
    },
    downloadCertificate(certificateId) {
      console.log('下载证书', certificateId);
    },
    submitPasswordChange() {
      if (this.passwordForm.newPassword !== this.passwordForm.confirmPassword) {
        this.$message.error('新密码与确认密码不一致');
        return;
      }
      console.log('修改密码', this.passwordForm);
    }
  }
};
</script>

<style scoped>
.main-container {
  display: flex;
  height: 100vh; /* 设置整个容器占满视口高度 */
}

.el-menu-vertical {
  width: 200px;
}

.content-container {
  flex-grow: 1;
  padding: 20px;
}

.info-display {
  margin-bottom: 20px;
}
</style>
