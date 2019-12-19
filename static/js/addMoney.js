var inOUT;
var cashIN = document.querySelector('.IN');
var cashOUT = document.querySelector('.OUT');
function cashINFUN(){
    cashIN.style.backgroundColor = "#7ff185";
    cashOUT.style.backgroundColor = '#FFFFFF';
    inOUT = 'I';
}
function cashOUTFUN(){
    cashOUT.style.backgroundColor = "#ffa5a5";
    cashIN.style.backgroundColor = '#FFFFFF';
    inOUT = 'O';
}
cashIN.addEventListener('click',cashINFUN)
cashOUT.addEventListener('click',cashOUTFUN)

var tag
var tagsALL = document.querySelectorAll('.typeTag');
for(x of tagsALL){
    x.addEventListener('click',choiceTag);
}
function choiceTag(event){
    for(i of tagsALL){
        i.style.backgroundColor = "#ffffff";
        i.style.color = '#acacac'
    }
    e = event.currentTarget
    e.style.backgroundColor = '#acacac';
    e.style.color = '#FFFFFF';
    tag = e.textContent.replace("#","");
    console.log(tag);

}

//--------------時間----------------------
var yearCon = document.querySelector(".year")
var mouthCon = document.querySelector(".mouth")
var dayCon = document.querySelector('.day')
var year_btn = document.querySelector(".year_btn")
var mouth_btn = document.querySelector(".mouth_btn")
var day_btn = document.querySelector('.day_btn')
var pro_btn = document.querySelector('.pro_btn')

var time_item_ALL = document.querySelectorAll('.dropdown-item')
for( x of time_item_ALL) {
    x.addEventListener('click',setTime)
}
function setTime(event){
    e = event.currentTarget
    if(e.parentElement == yearCon) year_btn.innerHTML = e.textContent
    else if(e.parentElement == mouthCon) mouth_btn.innerHTML = e.textContent
    else if(e.parentElement == dayCon)day_btn.innerHTML = e.textContent
    else pro_btn.innerHTML = e.textContent
    
    console.log(e)
    console.log(year_btn.textContent)
}

userID = 'try000'
grupID = "none"
function post_to_url(params, method) {
    method = method || "post"; // Set method to post by default, if not specified.

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", "/newMoney/");

    for(var key in params) {
        var hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", key);
        hiddenField.setAttribute("value", params[key]);
        form.appendChild(hiddenField);
    }

    document.body.appendChild(form);    // Not entirely sure if this is necessary
    form.submit();
    console.log(form)
}
var responseJSON
function tryFetch(data){
    let url = 'http://127.0.0.1:8000/newMoney/';
    console.log(data)
    fetch(url, {
        method: 'POST',
        // headers 加入 json 格式
        // headers: {
        //     'Content-Type': 'application/json'
        // },
        // body 將 json 轉字串送出
        body: data
    }).then((response) => {
            return response; 
        }).then((jsonData) => {
            responseJSON = jsonData
            console.log(jsonData);
        }).catch((err) => {
            console.log('錯誤:', err);
    })
}


var userID = document.querySelector('.userID')
var btn = document.querySelector('.btn-success')
var submitData
btn.addEventListener('click',function(){
    // var formData = new FormData();
    // formData.append("PorG", 'P');
    // formData.append("pName", pro_btn.textContent);
    // formData.append('PorG','P');
    // formData.append('pName',pro_btn.textContent);
    // formData.append('uID',userID.textContent);
    // formData.append('InorOut',inOUT);
    // formData.append('ItemType',tag);
    // formData.append('ItemName',document.querySelector('.ItemName').value);
    // formData.append('value',document.querySelector('.howmuch').value);

    submitData = {
        'addORedit':addORedit_flag,
        'PorG':'P',
        'pName':pro_btn.textContent,
        'uID':userID.textContent,
        'gpID':'None',
        'time':update[0].textContent,
        'InorOut':inOUT,
        'ItemType':tag,
        'ItemName':document.querySelector('.ItemName').value,
        'value':document.querySelector('.howmuch').value,
    }

    post_to_url(submitData);
    // tryFetch(formData)
    console.log(responseJSON)
})

var addORedit_flag = 'add';
var update = document.querySelectorAll('.update')
console.log(update)
console.log(update[0].textContent)
if(update[0].textContent != 'None'){
    console.log(123123)
    addORedit_flag = 'exit'
    if (update[1].textContent == 'I'){
        cashINFUN()
    }
    else if(update[1].textContent == 'O'){
        cashOUTFUN()
    }

    var tag_change
    for(i of tagsALL){
        i.style.backgroundColor = "#ffffff";
        i.style.color = '#acacac'
        if (i.textContent.replace("#","") == update[2].textContent){
            tag_change = i
        }
    }
    tag = update[2].textContent
    tag_change.style.backgroundColor = '#acacac';
    tag_change.style.color = '#FFFFFF';

    document.querySelector('.ItemName').value = update[3].textContent
    document.querySelector('.howmuch').value = update[4].textContent

}