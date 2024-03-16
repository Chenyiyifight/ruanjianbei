const { defineConfig } = require('@vue/cli-service')

module.exports = {
  ...defineConfig({
    transpileDependencies: true,
    lintOnSave: false // 关闭 eslint
  }),

  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  }
}
