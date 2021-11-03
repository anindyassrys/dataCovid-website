fetch('https://api.kawalcorona.com/indonesia')
.then((response)=>{
    return response.json();
})
.then((response)=>{
    console.log(res)
    var positif = document.getElementById('positif')

    positif.append(positif)
})