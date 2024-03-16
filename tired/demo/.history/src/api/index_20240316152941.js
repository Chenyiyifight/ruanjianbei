import http from '../utils/request'

//请求首页数据
export const getData = () =>{
    return http.get('/predict/data',)
}

export const getMenu = (data)=>{
    return http.post('/login',data)
}