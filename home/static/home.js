// fetch data from API
fetch('https://corona.lmao.ninja/v2/countries/indonesia')
.then((response)=>{
    return response.json();
})
.then((data)=>{
    document.getElementById("cases").innerHTML = data.cases;
    document.getElementById("todayCases").innerHTML = data.todayCases;
    
})
