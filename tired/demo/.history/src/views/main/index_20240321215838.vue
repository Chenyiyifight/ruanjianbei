<template>
    <div class="back">
        <el-container>
            <el-aside width="auto">
                <common-aside />
            </el-aside>
            <el-container>
                <el-header>
                    <common-header />
                </el-header>
                <el-main>
                    <router-view></router-view>
                </el-main>
                <div class="ai"> <ai /></div>
            </el-container>
        </el-container>
    </div>
</template>


<script>
import CommonAside from '../../components/CommonAside.vue'
import CommonHeader from '../../components/CommonHeader.vue'
import Ai from '../../components/AI.vue'

export default {
    data() {
        return {

        }
    },
    components: {
        CommonAside,
        CommonHeader,
        Ai
    }
}
</script>
<style scoped>
.el-header {
    padding: 0;
}

.back {
    background-color: rgb(219, 242, 240);
}

.bg-purple-dark {
    background: #99a9bf;
}
.ai {
    display: flex;
    justify-content: flex-end; /* 水平居中 */
    
    margin-top: 0px; /* 减小上边距 */
    margin-left: -5px; /* 向左移动 */
    height: 500px;
    width: 30%;
}
</style>
