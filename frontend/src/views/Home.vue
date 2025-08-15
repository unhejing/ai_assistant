<template>
  <div class="home">
    <section class="hero">
      <h1>若伊 · AI 生成工作台</h1>
      <p>使用自然语言创作高质量图像，未来可扩展到数字人、声音克隆和智能体</p>
      <el-button type="primary" size="large" @click="$router.push('/playground')">
        立即开始
      </el-button>
    </section>

    <section class="features">
      <el-card class="feature-card" v-for="f in features" :key="f.title">
        <h3>{{ f.title }}</h3>
        <p>{{ f.desc }}</p>
      </el-card>
    </section>
  </div>
</template>

<script setup lang="ts">
const features = [
  { title: '文生图', desc: '输入提示词，一键生成图片' },
  { title: '图生图', desc: '上传图片，结合提示词改造风格' },
  { title: '可扩展架构', desc: '即插即用，便于集成数字人、声音克隆、智能体模块' },
]
</script>

<style scoped>
.home {
  padding: 24px;
}
.hero {
  text-align: center;
  margin: 48px 0;
}
.features {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
.feature-card {
  background: #111318;
  color: #e5e7eb;
}
</style>