var log = function(){
    console.log(arguments)
}

var api = {}
api.ajax = function(url, method, form, callback){
    var request = {
        url: url,
        type: method,
        data: form,
        success: function(response){
            var r = JSON.parse(response)
            callback(r)
        },
        error: function(){
            var r = {
                success: false,
                message: '网络中断',
            }
            callback(r)
        }
    }
    $.ajax(request)
}

api.todoAdd = function(form, callback){
    var url = '/api/add'
    var method = 'post'
    api.ajax(url, method, form, callback)
}
api.todoDelete = function(url, callback){
    var method = 'get'
    var form = {}
    api.ajax(url, method, form, callback)
}
api.todoUpdate = function(url, form, callback){
    var method = 'post'
    api.ajax(url, method, form, callback)
}
