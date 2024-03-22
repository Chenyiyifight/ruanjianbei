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
                    <div>
                        <el-row>
                            <el-col :span="10">
                                <div class="grid-content bg-purple-dark"></div>
                            </el-col>
                        </el-row>
                    </div>
                    <router-view></router-view>
                </el-main>

            </el-container>
        </el-container>
    </div>
</template>


<script>
import CommonAside from '../../components/CommonAside.vue'
import CommonHeader from '../../components/CommonHeader.vue'
//import CommonHeader from '../../components/Aicy.vue'

export default {
    data() {
        return {

        }
    },
    components: {
        CommonAside,
        CommonHeader,
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

.el-row {
    margin-bottom: 20px;

    &:last-child {
        margin-bottom: 0;
    }
}

.el-col {
    border-radius: 4px;
}

.bg-purple-dark {
    background: #99a9bf;
}

.bg-purple {
    background: #d3dce6;
}

.bg-purple-light {
    background: #e5e9f2;
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}

.row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
}
</style>
