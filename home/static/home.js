// // panggil function getGlobalInfo ketika halaman sudah berhasil di load
// $(document).ready(function(){
//     getIndonesiaInfo();
// });

// // membuat fungsi untuk mendapatkan jumlah di negara Indonesia
// function getIndonesiaInfo(){
//     $.ajax({
//         url : 'https://coronavirus-19-api.herokuapp.com/countries/Indonesia',
//         success: function (data) {

//             try{
//                 var json = data;
//                 var positif = json.todayCases;

//                 $("positif").html(positif);
//             }catch(e){
//                 alert("Gagal mendapatkan data dari server")
//             }
//         }, error : function(resp) {

//         }
//     });
// }
// fetch data from API
fetch('https://corona.lmao.ninja/v2/countries/indonesia')
.then((response)=>{
    return response.json();
})
.then((data)=>{
    document.getElementById("todayCases").innerHTML = data.todayCases;
})
