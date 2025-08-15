<template>
  <div class="playground">
    <div class="left-panel">
      <el-form label-width="80px" label-position="top" class="control-form">
        <el-form-item label="提示词">
          <el-input v-model="prompt" type="textarea" :rows="3" placeholder="请输入你的创意描述，如：一只穿宇航服的柯基，赛博朋克风" />
        </el-form-item>
        <el-form-item label="尺寸">
          <el-select v-model="size">
            <el-option label="512x512" value="512x512" />
            <el-option label="768x768" value="768x768" />
            <el-option label="1024x1024" value="1024x1024" />
          </el-select>
        </el-form-item>
        <el-form-item label="步数">
          <el-slider v-model="steps" :min="10" :max="60" />
        </el-form-item>
        <el-form-item label="引导强度">
          <el-slider v-model="guidance" :min="1" :max="15" :step="0.5" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" :loading="loading" @click="onGenerate">生成</el-button>
          <el-button @click="onReset">重置</el-button>
        </el-form-item>
      </el-form>

      <el-divider>图生图</el-divider>
      <el-upload
        class="upload-demo"
        drag
        action="/api/images/img2img"
        :on-success="handleUploadSuccess"
      >
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
      </el-upload>
    </div>

    <div class="right-panel">
      <el-card class="result-card" shadow="hover">
        <template #header>
          <div class="card-header">
            <span>生成结果</span>
            <el-button type="primary" link @click="onDownload" :disabled="!imageUrl">下载</el-button>
          </div>
        </template>
        <div class="result">
          <img v-if="imageUrl" :src="imageUrl" alt="生成结果" />
          <div v-else class="placeholder">等待生成...</div>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'
import { saveAs } from 'file-saver'

const prompt = ref('')
const size = ref('512x512')
const steps = ref(30)
const guidance = ref(7.5)
const loading = ref(false)
const imageUrl = ref('')

function onReset() {
  prompt.value = ''
  size.value = '512x512'
  steps.value = 30
  guidance.value = 7.5
  imageUrl.value = ''
}

async function onGenerate() {
  loading.value = true
  try {
    const [w, h] = size.value.split('x').map(Number)
    const resp = await axios.post('/api/images/txt2img', {
      prompt: prompt.value,
      steps: steps.value,
      guidance_scale: guidance.value,
      width: w,
      height: h,
    })
    imageUrl.value = resp.data.image_path
  } catch (e) {
    console.error(e)
  } finally {
    loading.value = false
  }
}

function handleUploadSuccess(res: any) {
  imageUrl.value = res.image_path
}

function onDownload() {
  if (!imageUrl.value) return
  saveAs(imageUrl.value, 'result.png')
}
</script>

<style scoped>
.playground {
  display: grid;
  grid-template-columns: 360px 1fr;
  gap: 16px;
  padding: 16px;
}
.left-panel {
  background: #111318;
  padding: 16px;
  border: 1px solid #1f2937;
}
.right-panel .result-card {
  background: #111318;
}
.result {
  min-height: 480px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.placeholder {
  color: #6b7280;
}
.result img { max-width: 100%; border-radius: 8px; }
</style>