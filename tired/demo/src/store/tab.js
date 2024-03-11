export default{
    state:{
        isCollapse:false //控制菜单展开收起
    },
    mutations:{
        collapseMenu(state){
            state.isCollapse= !state.isCollapse
        }
    }

}