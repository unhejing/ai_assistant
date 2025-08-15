<template>
  <div class="layout">
    <HeaderBar />
    <div class="content">
      <router-view />
    </div>
  </div>
</template>

<script setup lang="ts">
import HeaderBar from './components/HeaderBar.vue'
</script>

<style scoped>
.layout {
  display: flex;
  flex-direction: column;
  height: 100vh;
  background: #0f0f12; /* 深色背景，模仿若伊风格 */
}
.content {
  flex: 1;
  overflow: auto;
}
</style>