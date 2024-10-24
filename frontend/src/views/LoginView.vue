<template>
  <FormContainer
    welcomeTitle="欢迎使用平台"
    welcomeMessage="请输入您的账号信息并选择身份进行登录，享受我们的服务"
    buttonText="了解更多"
  >
    <!-- 表单部分通过插槽传递 -->
    <template v-slot:form>
      <h2 class="login-title">登录</h2>

      <!-- 身份选择 -->
      <el-form :model="loginForm" class="login-form">
        <el-form-item>
          <el-radio-group v-model="loginForm.role" size="large">
            <el-radio label="student">学生登录</el-radio>
            <el-radio label="teacher">教师登录</el-radio>
          </el-radio-group>
        </el-form-item>

        <!-- 账号 -->
        <el-form-item>
          <el-input
            v-model="loginForm.username"
            placeholder="请输入账号"
            class="input-field"
            prefix-icon="el-icon-user"
            size="large"
          />
        </el-form-item>

        <!-- 密码 -->
        <el-form-item>
          <el-input
            v-model="loginForm.password"
            placeholder="请输入密码"
            type="password"
            class="input-field"
            prefix-icon="el-icon-lock"
            size="large"
          />
        </el-form-item>

        <!-- 验证码 -->
        <el-form-item>
          <el-input
            v-model="loginForm.captcha"
            placeholder="请输入验证码"
            class="input-field"
            size="large"
          />
          <!-- 验证码图片 -->
          <img :src="captchaImageSrc" alt="验证码" class="captcha-image" @click="refreshCaptcha">
        </el-form-item>

        <!-- 登录按钮 -->
        <el-form-item>
          <el-button type="primary" class="login-btn" @click="onLogin">登录</el-button>
        </el-form-item>
      </el-form>

      <!-- 登录选项 -->
      <div class="login-options">
        <router-link to="/forgot-password" class="forgot-password-link">忘记密码?</router-link>
        <p>没有账号? <router-link to="/signup" class="signup-link">立即注册</router-link></p>
      </div>
    </template>
  </FormContainer>
</template>

<script>
import FormContainer from '@/components/FormContainer.vue';

export default {
  name: 'LoginView',
  components: {
    FormContainer,
  },
  data() {
    return {
      loginForm: {
        role: null, // 默认身份选择为空
        username: '',
        password: '',
        captcha: '' // 验证码字段
      },
      captchaImageSrc: 'path_to_captcha_image', // 验证码图片路径
    };
  },
  methods: {
    onLogin() {
      if (this.loginForm.username && this.loginForm.password && this.loginForm.captcha) {
        // 模拟登录成功，触发 'login' 事件并传递 role 和 isLogin 状态
        this.$emit('login', this.loginForm.role, true);
        this.$router.push('/'); // 登录成功后跳转到首页
      } else {
        this.$message.error('请填写完整的登录信息');
      }
    },
    refreshCaptcha() {
      // 刷新验证码逻辑，重新加载验证码图片
      this.captchaImageSrc = 'path_to_new_captcha_image'; // 根据需要更改为实际逻辑
    }
  }
};
</script>

<style scoped>
/* 标题和副标题样式 */
.login-title {
  font-size: 1.8rem;
  margin-bottom: 10px;
  text-align: center;
  font-weight: bold;
}

/* 表单样式 */
.login-form {
  width: 100%;
}

/* 输入框样式 */
.input-field {
  width: 100%;
  margin-bottom: 15px;
}

/* 验证码图片样式 */
.captcha-image {
  display: block;
  margin-top: 10px;
  max-width: 150px;
  cursor: pointer;
}

/* 登录按钮样式 */
.login-btn {
  width: 100%;
  height: 50px;
  font-size: 1rem;
  background-color: #1d2430;
  color: white;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.login-btn:hover {
  background-color: #3a3f51;
}

/* 登录选项链接 */
.login-options {
  margin-top: 10px;
  text-align: center;
}

.forgot-password-link, .signup-link {
  color: #409eff;
  text-decoration: none;
}

.forgot-password-link:hover, .signup-link:hover {
  text-decoration: underline;
}
</style>
