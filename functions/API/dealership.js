/**
  *
  * main() 将在调用此操作时运行
  *
  * @param Cloud Functions 操作接受单个参数，该参数必须为 JSON 对象。
  *
  * @return 此操作的输出，必须为 JSON 对象。
  *
  */
 const { CloudantV1 } = require('@ibm-cloud/cloudant');
 const { IamAuthenticator } = require('ibm-cloud-sdk-core');
 const setting = 
 {
     "COUCH_URL": "https://1bbf4835-720f-4b1b-be1a-70d899dfc677-bluemix.cloudantnosqldb.appdomain.cloud",
     "IAM_API_KEY": "S27CFTIaQ_MSLLyGbzWV2qSyETVquhXAf7dl5dEEOvyI",
 }
 function parseQueryString(queryString) {
     const params = {};
     const keyValuePairs = queryString.split('&');
     
     for (const pair of keyValuePairs) {
         const [key, value] = pair.split('=');
         params[key] = value;
     }
     
     return params;
 }
 
 async function main(params) {
       const authenticator = new IamAuthenticator({ apikey: setting.IAM_API_KEY })
       const cloudant = CloudantV1.newInstance({
           authenticator: authenticator
       });
       cloudant.setServiceUrl(setting.COUCH_URL);
       
       params = await parseQueryString(params["__ow_query"]);
       if(params.hasOwnProperty("state")){
           var state  = params.state;
           console.log(state);
           let response = await cloudant.postFind({
             db: 'dealerships', // Name of the database
             selector: {
                 state: { $eq: state } // Example search condition
             }
             });
             
           return {"body":{"rows":response.result.docs}};
       }
       
       else{
       let response = await cloudant.postAllDocs({
           db:"dealerships",
           includeDocs: true
       });
       let rows = response.result.rows.map(item=>item.doc);
       return {"body":{"rows":rows}};
       }
 }
 