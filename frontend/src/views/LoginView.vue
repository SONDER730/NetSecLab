<template>
  <div class="login-view">
    <el-tabs v-model="activeTab" @tab-click="handleTabClick" class="login-tabs">
      <!-- 学生登录 -->
      <el-tab-pane label="学生登录" name="student">
        <el-form ref="studentLoginForm" :model="studentLoginForm" label-width="80px" class="login-form">
          <el-form-item label="学号">
            <el-input v-model="studentLoginForm.username" placeholder="请输入学生用户名"></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input type="password" v-model="studentLoginForm.password" placeholder="请输入密码"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit('student')">登录</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>

      <!-- 教师登录 -->
      <el-tab-pane label="教师登录" name="teacher">
        <el-form ref="teacherLoginForm" :model="teacherLoginForm" label-width="80px" class="login-form">
          <el-form-item label="工号">
            <el-input v-model="teacherLoginForm.username" placeholder="请输入教师用户名"></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input type="password" v-model="teacherLoginForm.password" placeholder="请输入密码"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="onSubmit('teacher')">登录</el-button>
          </el-form-item>
        </el-form>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      activeTab: 'student', // 默认激活学生登录
      // 学生登录表单数据
      studentLoginForm: {
        username: '',
        password: ''
      },
      // 教师登录表单数据
      teacherLoginForm: {
        username: '',
        password: ''
      }
    };
  },
  methods: {
    // Tab 点击处理
    handleTabClick(tab) {
      this.activeTab = tab.name;
    },
    // 表单提交处理，自动判断当前登录身份并处理
    onSubmit(role) {
      if (role === 'student') {
        if (this.studentLoginForm.username && this.studentLoginForm.password) {
          this.$message.success('学生登录成功！');
          // 处理学生登录后的逻辑
          this.$emit('login', 'student'); // 向父组件传递身份信息
          this.$router.push('/studentInfo'); // 跳转到学生界面
        } else {
          this.$message.error('请填写学生用户名和密码');
        }
      } else if (role === 'teacher') {
        if (this.teacherLoginForm.username && this.teacherLoginForm.password) {
          this.$message.success('教师登录成功！');
          // 处理教师登录后的逻辑
          this.$emit('login', 'teacher'); // 向父组件传递身份信息
          this.$router.push('/TeacherInfo'); // 跳转到教师界面
        } else {
          this.$message.error('请填写教师用户名和密码');
        }
      }
    }
  }
};
</script>

<style scoped>

.login-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  padding-left: 20px;
  padding-right: 20px;
  background-color: #f5f5f5;
}

h1 {
  font-size: 2rem;
  margin-bottom: 20px;
  color: #409EFF;
}

.login-tabs {
  width: 400px;
  }

.login-form {
  background-color: #fff;
  padding: 40px 40px 20px 20px;
  border-radius: 8px;
  box-shadow: 0px 2px 12px rgba(0, 0, 0, 0.1);
}

.el-form-item {
  margin-bottom: 20px;
}
</style>
