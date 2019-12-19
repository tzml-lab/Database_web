function changeMode(event){
    var button = event.currentTarget;

    var contexts = document.querySelectorAll('.contexts');
    for(var context of contexts){
        context.style.display = 'none';
    }
    switch(button.innerText){
        case '收入':
            var context = document.querySelector('#IN_cons');
            context.style.display = null;
            break;
        case '支出':
            var context = document.querySelector('#OUT_cons');
            context.style.display = null;
            break;
        case '圖表':
            var context = document.querySelector('#CHART_cons');
            context.style.display = null;
    }
}
var moneyJsons = {}
function changePro(event){
    // var sel = document.querySelector('#project div select');
    choicePro_name = $('#project div select option:selected').text();
    console.log(choicePro_name);
    if(choicePro_name === proName)
        return;

    fetch('/api/projMoney/'+userID+'?pName='+choicePro_name)
        .then(function(response) {
            return response.json();
        })
        .then(myJson =>{
            var intervalID = scope.setInterval(1000)
            moneyJsons = JSON.parse(myJson);
            console.log(myJson);
        });
        console.log(moneyJsons);

    //刪掉收入
    var inItems = document.querySelectorAll('#IN_cons .item');
    for(var inItem of inItems){
        inItem.remove();
    }
    //var parent = document.getElementById('IN_cons');
    for(var json in moneyJsons){
        console.log(json);
    }
    // var newChild = '<p>Child ' + childNumber + '</p>';
    // parent.insertAdjacentHTML('beforeend', newChild);
    // childNumber++;

    //刪掉支出
}
function delMoney(event){
    
    var moneyPK = event.currentTarget.parentNode.parentNode.querySelector('.beforeFour .con_date');
    console.log(moneyPK.innerText);

    var url = '/api/delMoney/';
    // var data = {userID:userID, moneyPK:moneyPK.innerText}
    var formData = new FormData();
    
    formData.append("userID", userID);
    formData.append("moneyPK", moneyPK.innerText);
    fetch(url, {
        method: 'POST',

        body: formData
      }).then((response) => {
        console.log("well"); 
        }).catch((err) => {
          console.log('錯誤:', err);
      })
    var money = event.currentTarget.parentNode.parentNode;
    money.remove();
    
}



//使用者ID
var userID = $('#pro_user').text();
var proName = $('#pro_name').text();
console.log(userID);
console.log(proName);

//choiceDel刪除money
var choiceDels = document.querySelectorAll('.afterFour .delete');
for(var choiceDel of choiceDels){
    choiceDel.addEventListener('click',delMoney);
}

//choicePro選擇個人專案
var choicePro = document.querySelector('#choicePro');
choicePro.addEventListener('click', changePro);

//button選收入.支出.圖表
var buttons = document.querySelectorAll('#modes div');
for(var button of buttons){
    button.addEventListener('click',changeMode);
}