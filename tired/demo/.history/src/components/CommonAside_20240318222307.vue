<template>
  <el-menu
    default-active="1-4-1"
    class="el-menu-vertical-demo"
    @open="handleOpen"
    @close="handleClose"
    :collapse="isCollapse"
    background-color="#E3DCF7"
    text-color="#2F4F4F"
    active-text-color="#79B8D9">
    <h3>{{!isCollapse ? '机器学习模型' : 'Model'}}</h3>
    <el-menu-item
     @click="clickMenu(item)"
      v-for="item in noChildren"
      :key="item.data"
      :index="item.name"
    >
      <i :class="`el-icon-${item.icon}`"></i>
      <span slot="title">{{ item.label }}</span>
    </el-menu-item>
    <el-submenu v-for="item in hasChildren" :key="item.label" :index="1">
      <template slot="title">
        <i :class="`el-icon-${item.icon}`"></i>
        <span slot="title">{{ item.label }}</span>
      </template>
      <el-menu-item-group v-for="SubItem in item.children" :key="SubItem.name">
        <el-menu-item :index="SubItem.name">{{ SubItem.label }}</el-menu-item>
      </el-menu-item-group>
    </el-submenu>
  </el-menu>
</template>

<style lang="less" scope>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.el-menu{
    height: 100vh;
    h3{
        color:#313D48;
        text-align: center;

    }

}
.el-menu-item{
    font-size: 16px;
}
</style>


<script>
export default {
  data() {
    return {
      menuData: [
        {
          path: "/home",
          name: "home",
          label: "Home",
          icon: "s-home",
          url: "Home/Home",
        },
        {
          path: "/train",
          name: "train",
          label: "模型训练",
          icon: "document",
          url: "train/train",
        },
        {
          path: "/forecast",
          name: "forecast",
          label: "预测",
          icon: "edit",
          url: "forecast/forecast",
        },
        {
          path: "/show",
          name: "show",
          label: "结果展示",
          icon: "pie-chart",
          url: "show/show",
        },
        {
          path: "/ai",
          name: "ai",
          label: "AI",
          icon: "pie-chart",
          url: "ai/ai",
        },
        {
          label: "其他",
          icon: "location",
          children: [
            {
              path: "/page1",
              name: "page1",
              label: "AIcy",
              icon: "setting",
              url: "Other/PageOne",
            },
            {
              path: "/page2",
              name: "page2",
              label: "神经病",
              icon: "setting",
              url: "Other/PageTwo",
            },
          ],
        },
      ],
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    //点击菜单
    clickMenu(item){
      console.log(item);
      //当页面路由与跳转不一样时允许跳转
      if(this.$route.path!=item.path){
        this.$router.push(item.path)
      }

    }
  },
  computed: {
    //没有子菜单
    noChildren() {
      return this.menuData.filter((item) => !item.children);
    },
    //有子菜单
    hasChildren() {
      return this.menuData.filter((item) => item.children);
    },
    isCollapse(){
      return this.$store.state.tab.isCollapse
    }
  },
};
</script>