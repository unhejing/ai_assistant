<template>
  <div class="header">
    <div class="left">
      <span class="logo">即梦·Workbench</span>
      <el-menu mode="horizontal" :default-active="active" background-color="#0f0f12" text-color="#cbd5e1" active-text-color="#60a5fa" @select="onSelect">
        <el-menu-item index="/">首页</el-menu-item>
        <el-menu-item index="/playground">工作台</el-menu-item>
      </el-menu>
    </div>
    <div class="right">
      <el-button type="primary" @click="$router.push('/playground')">开始创作</el-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const active = ref(route.path)

watch(
  () => route.path,
  (val) => {
    active.value = val
  },
)

function onSelect(index: string) {
  router.push(index)
}
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 16px;
  height: 56px;
  border-bottom: 1px solid #1f2937;
}
.left {
  display: flex;
  align-items: center;
  gap: 24px;
}
.logo {
  font-weight: 600;
  color: #e5e7eb;
}
</style>