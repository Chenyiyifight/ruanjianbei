const { defineConfig } = require('@vue/cli-service')

module.exports = {
  ...defineConfig({
    transpileDependencies: true,
    lintOnSave: false // 关闭 eslint
  }),

  devServer: {
    proxy: {
      '/api': {
        target: ' http://127.0.0.1:8000/',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  }
}
