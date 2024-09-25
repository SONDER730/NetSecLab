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
  background-color: rgba(255, 255, 255, 0.8); /* 半透明背景 */
  backdrop-filter: blur(5px); /* 背景模糊效果 */
  border-radius: 12px;
  //box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2); /* 较大的阴影 */
  position: relative;
  z-index: 1;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 30px;
  color: #409EFF;
  text-shadow: 1px 1px 6px rgba(0, 0, 0, 0.1); /* 添加文字阴影 */
}

.login-tabs {
  width: 400px;
  background-color: #fff; /* 背景颜色 */
  border-radius: 8px;
  box-shadow: 0px 6px 20px rgba(0, 0, 0, 0.1); /* 更大的阴影 */
  padding: 20px;
}

.login-form {
  background-color: #f9f9f9; /* 浅灰色背景 */
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0px 4px 16px rgba(0, 0, 0, 0.1); /* 适中的阴影 */
  border: 1px solid #e0e0e0; /* 边框颜色 */
}

.el-form-item {
  margin-bottom: 25px; /* 表单项间隔更大 */
}

.el-button {
  width: 100%;
  height: 45px;
  font-size: 1.1rem; /* 按钮文字大小 */
  background-color: #409eff;
  color: white;
  border-radius: 6px;
}

.el-button:hover {
  background-color: #66b1ff; /* 按钮悬停颜色 */
}



/* 调整背景模糊效果 */
body {
  overflow: hidden; /* 防止滚动条出现 */
}

</style>

