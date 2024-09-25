<template>
  <div class="announcement-view">
    <!-- 左侧竞赛列表部分 -->
    <el-row >
      <el-col :span="16" class="left-section">
        <!-- 搜索功能 -->
        <div class="search-bar">
          <el-input
            placeholder="请输入关键字搜索竞赛"
            v-model="searchQuery"
            prefix-icon="el-icon-search"
            @input="handleSearch"
          />
        </div>

        <!-- 滚动竞赛列表 -->
        <div class="competition-list">
          <el-card
            v-for="competition in filteredCompetitions"
            :key="competition.id"
            class="competition-item"
            @click="viewCompetition(competition.id)"
          >
            <h3>{{ competition.title }}</h3>
            <p>{{ competition.date }}</p>
            <p>{{ competition.description }}</p>
          </el-card>
        </div>
      </el-col>

      <!-- 右侧个人信息部分 -->
      <el-col :span="8" class="right-section">
        <div class="user-info">
          <h3>Welcome, {{ userName }}</h3>
          <p>Type: {{ userType }}</p>
          <p>Questions: {{ userQuestions }}</p>
          <p>Answers: {{ userAnswers }}</p>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      competitions: [
        { id: 1, title: '竞赛1', date: '2024-09-25', description: '描述内容1' },
        { id: 2, title: '竞赛2', date: '2024-10-01', description: '描述内容2' },
        // 更多竞赛条目...
      ],
      userName: '1111111',
      userType: '张三',
      userQuestions: 3,
      userAnswers: 4,
    };
  },
  computed: {
    filteredCompetitions() {
      if (this.searchQuery) {
        return this.competitions.filter(c =>
          c.title.includes(this.searchQuery) || c.description.includes(this.searchQuery)
        );
      }
      return this.competitions;
    },
  },
  methods: {
    handleSearch() {
      // 处理搜索的逻辑，可以直接过滤展示的竞赛
      console.log('搜索关键字:', this.searchQuery);
    },
    viewCompetition(id) {
      console.log('查看竞赛详情:', id);
      // 跳转到竞赛详情页面
      this.$router.push(`/competition/${id}`);
    },
  },
};
</script>

<style scoped>
.announcement-view {
  //display: flex;
  width: 100%;
  //padding: 20px;
}

.left-section {
  padding: 10px;
  background-color: #f5f5f5;
}

.search-bar {
  margin-bottom: 20px;
}

.competition-list {
  max-height: 80vh;
  overflow-y: auto;
}

.competition-item {
  margin-bottom: 10px;
  cursor: pointer;
  transition: 0.3s;
}

.competition-item:hover {
  box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.1);
}

.right-section {
  padding: 20px;
  background-color: #fff;
  text-align: center;
}

.user-info {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

</style>
