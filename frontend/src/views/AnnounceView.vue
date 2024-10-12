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
      <el-menu-item index="awards">
        奖项竞赛
      </el-menu-item>
      <el-menu-item index="experts">
        人才专家
      </el-menu-item>
      <el-menu-item index="tools">
        科研工具
      </el-menu-item>
    </el-menu>

    <!-- 右侧内容区域 -->
    <div class="content-container">
      <!-- 奖项竞赛部分 -->
      <div v-if="activeMenu === 'awards'">
        <el-row :gutter="20" class="search-section">
          <el-col :span="5">
            <el-select v-model="searchMethod" placeholder="请选择检索方式">
              <el-option label="标题检索" value="title"></el-option>
              <el-option label="举办单位检索" value="organization"></el-option>
            </el-select>
          </el-col>

          <el-col :span="8">
            <el-input v-model="searchQuery" placeholder="请输入检索内容"></el-input>
          </el-col>

          <el-col :span="4">
            <el-date-picker v-model="startDate" type="date" placeholder="起始时间"></el-date-picker>
          </el-col>

          <el-col :span="4">
            <el-date-picker v-model="endDate" type="date" placeholder="结束时间"></el-date-picker>
          </el-col>

          <el-col :span="2">
            <el-button type="primary" @click="search">检索</el-button>
          </el-col>
        </el-row>

        <!-- 数据表格 -->
        <el-table :data="awardsData" stripe style="background-color: white;">
          <el-table-column prop="status" label="状态" width="150"></el-table-column>
          <el-table-column prop="title" label="标题"></el-table-column>
          <el-table-column prop="organization" label="发布机构" width="200"></el-table-column>
          <el-table-column prop="scope" label="范围" width="150"></el-table-column>
          <el-table-column prop="officialDate" label="官方日期" width="180"></el-table-column>
          <el-table-column prop="deadline" label="截止日期" width="180"></el-table-column>
        </el-table>
      </div>

      <!-- 人才专家部分 -->
      <div v-if="activeMenu === 'experts'">
        <el-row :gutter="20" class="search-section">
          <el-col :span="6">
            <el-select v-model="searchMethod" placeholder="请选择检索方式">
              <el-option label="姓名检索" value="name"></el-option>
              <el-option label="学院检索" value="school"></el-option>
            </el-select>
          </el-col>

          <el-col :span="8">
            <el-input v-model="searchQuery" placeholder="请输入检索内容"></el-input>
          </el-col>

          <el-col :span="2">
            <el-button type="primary" @click="search">检索</el-button>
          </el-col>
        </el-row>

        <!-- 数据表格 -->
        <el-table :data="expertsData" stripe style="background-color: white;">
          <el-table-column prop="name" label="姓名" width="150"></el-table-column>
          <el-table-column prop="school" label="学院"></el-table-column>
          <el-table-column prop="intro" label="简介"></el-table-column>
        </el-table>
      </div>

      <!-- 科研工具部分 -->
      <div v-if="activeMenu === 'tools'">
        <h2>科研工具</h2>
        <p>这里是科研工具部分的内容。</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeMenu: 'awards', // 默认选中的是奖项竞赛部分
      searchMethod: 'title', // 默认检索方式
      searchQuery: '', // 检索内容
      startDate: null, // 起始时间
      endDate: null, // 结束时间
      // 示例数据
      awardsData: [
        { status: '未截止', title: '2024年网络安全竞赛', organization: '北京邮电大学', scope: '全国', officialDate: '2024-09-25', deadline: '2024-10-15' },
        // 更多数据...
      ],
      expertsData: [
        { name: '张三', school: '计算机学院', intro: '网络安全专家，专注于安全加密与渗透测试。' },
        // 更多数据...
      ],
    };
  },
  methods: {
    handleMenuSelect(index) {
      this.activeMenu = index;
    },
    search() {
      console.log('检索方式:', this.searchMethod, '检索内容:', this.searchQuery);
      // 这里可以根据检索条件过滤数据
    },
  },
};
</script>

<style scoped>
.main-container {
  display: flex;
  height: 100vh;
  background-color: #001f3f;
}

/* 左侧菜单样式 */
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

/* 检索区域样式 */
.search-section {
  margin-bottom: 20px;
}

.el-table {
  background-color: #fff;
  width: 100%;
}

.el-menu-item {
  color: #fff !important;
  border-bottom: white;
}

.el-menu-item:hover {
  background-color: #409eff !important;
}
</style>
