import Mock from 'mockjs'
import permission from './mockServeData/permission';

//定义Mock请求拦截
// Mock.mock('/predict/data', function () {
//     console.log('拦截到了');
//     return [1.11, []]
// })

//Mock.mock('/api/login', 'post', permission.getMenu)