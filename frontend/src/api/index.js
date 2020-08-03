//aixos request response설정 
import axios from 'axios';

const config = {
   AIUrl :'http://localhost:8070/',  //ai
   BaseUrl :'http://localhost:8090/' //backend 
}

//AI로 이미지 + 비디오 전송 
function postAIData(){
    return axios.post(`${config.AIUrl}`); 
}

function SignIn(){
    return axios.post(`${config.BaseUrl}/signIn`);
}

export {
    postAIData,
    SignIn
}