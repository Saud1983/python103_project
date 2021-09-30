<script type="text/javascript">


var Choice= "Y";
var account = 0;

var ATMCard=parseInt(prompt("Please enter ATM Card Number", "<enter ATM Card here>"));


if ((ATMCard<=99999999) && (ATMCard>999999999)){
99999999
999999999
window.alert("Card ID Is Not Correct");


}

else{


document.write("Your Aaccount is: ",account,"\n");
window.alert("Welcom Mr.Saud ");
window.alert("Your Aaccount is: ",account,"\n");
var service = parseInt(prompt("Please enter 1 for Deposit\n 2 for Transfer Money\n  3 for Bill Payment\n", "<enter your choice here>"));


do {


while(service !=0){

if (service==1){

window.alert("Welcom to Money Depositing Service ");
var deposit=parseInt(prompt("Please enter your Deposit value", "<enter your deposit value here>"));
document.write("Your Deposit is: ",deposit,"\n");
window.alert("Please Comfirm to proceed Deposit");
account = account+deposit;
document.write("Your Aaccount is: ",account,"\n");
service =0;
 }



if (service==2){
window.alert("Welcom to Money Ttransfering Service ");
var transfered=parseInt(prompt("Please enter Money transfered value", "<enter Money transfered here>"));
document.write("Your Bill Value is: ",transfered,"\n");
window.alert("Please Comfirm to proceed transfering");
account = account-transfered;
document.write("Your Aaccount is: ",account,"\n");
service =0;
}


if (service==3){
window.alert("Welcom to Billing Payments Service");
var bill=parseInt(prompt("Please enter your bill value", "<enter bill value here>"));
document.write("Your Bill Value is: ",bill,"\n");
window.alert("Please Comfirm to proceed payment");
bill = bill-bill;
account = account-bill;
document.write("Your Bill is: ",bill,"\n");
document.write("Your Aaccount is: ",account,"\n");
service =0;
}


var service = parseInt(prompt("Please enter 1 for Deposit, 2 for Transfer, 3 for Bill Payment OR 0 for END", "<enter your choice here>"));


}

var Choice = prompt("Please enter \"Y\" to go to services, \"N\" to exit", "<enter your choice here>");


} while(Choice=="Y");

window.alert("GoodBye");

}

</script>
