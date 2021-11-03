function exit() {
    document.getElementById('delete').style.display='none';
    document.getElementById('edit').style.display='none'
}

function deleteItem() {
    exit();
}

var Jak = '{{ vaksinsJak }}';
var Bog = '{{ vaksinsBog }}';
var Dep = '{{ vaksinsDep }}';
var Tag = '{{ vaksinsTag }}';
var Bek = '{{ vaksinsBek }}';
function loaded() {
    $(document).ready(function() { 
        console.log(Jak);
        console.log(Bog);
        console.log(Dep);
        console.log(Tag);
        console.log(Bek);
        // alert("tes");
    });
}