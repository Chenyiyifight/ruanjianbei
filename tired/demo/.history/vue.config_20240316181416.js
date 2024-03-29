const { defineConfig } = require('@vue/cli-service')

module.exports = {
  ...defineConfig({
    transpileDependencies: true,
    lintOnSave: false // 关闭 eslint
  }),

  devServer: {
    proxy: {
      '/': {  
        target: 'localhost:8080',
        changeOrigin: true
      }
    }
  }
}
