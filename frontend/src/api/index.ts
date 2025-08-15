import axios from 'axios'

// 创建axios实例，统一设置baseURL
const api = axios.create({
  baseURL: '/api',
  timeout: 30000,
})

// 请求拦截器
api.interceptors.request.use((config) => {
  return config
})

// 响应拦截器
api.interceptors.response.use(
  (res) => res,
  (err) => {
    console.error('API Error:', err)
    return Promise.reject(err)
  },
)

export default api