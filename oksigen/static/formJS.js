function required(){
    var urlcek = document.forms["form"]["url"].value;
    var alamatcek = document.forms["form"]["alamat"].value;
    var teleponcek = document.forms["form"]["telepon"].value;
    var domisilicek = document.forms["form"]["domisili"].value;

    if (urlcek == "" || alamatcek == "" || teleponcek == "" || domisilicek == ''){
        alert("Please fill all data in the form");
        return false;
    }
    else{
        alert("Data berhasil ditambahkan.");
        return true;
    }
}