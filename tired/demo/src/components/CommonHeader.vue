<template>
    <div class="header-container">
        <div class="l-content">
            <el-button @click="handleMenu" type="primary" icon="el-icon-menu" circle></el-button>
            <span class="text">首页</span>
        </div>
        <div class="r-content">
            <el-dropdown>
                <span class="el-dropdown-link">
                    <img class="user" src="../assets/images/user.png" alt="">
                </span>
                <el-dropdown-menu slot="dropdown">
                    <el-dropdown-item>用户中心</el-dropdown-item>
                    <el-dropdown-item @click.native="layout">退出</el-dropdown-item>
                </el-dropdown-menu>
            </el-dropdown>
        </div>

    </div>
</template>

<script>
import Cookie from 'js-cookie';
export default {
    data() {
        return {}
    },
    methods: {
        handleMenu() {
            this.$store.commit('collapseMenu')
        },
        layout(){
            //清楚cookie中token
            Cookie.remove('token')
            this.$router.push('/login')
        }
    }
}
</script>


<style lang="less" scoped>
.header-container {
    padding: 0 20px;
    background-color: rgb(196, 226, 255);
    height: 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;

    .text {
        font-size: 16px;
        margin-left: 10px;
    }

    .r-content {
        .user {
            width: 45px;
            height: 45px;
            border-radius: 50%;
        }
    }
}
</style>