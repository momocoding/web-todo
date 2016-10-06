
var addTemplate = function(todo){
    var t = `
               <div class="todo-cell clear-fix" data-id="${ todo.id}">
                   <div class="todo-content left">
                       ${ todo.task }
                   </div>
                   <div class="right">
                       <button class="todo-button-delete"> 完成</button>
                       <button class="todo-button-update"> 修改</button>
                   </div>
                   <div class="right tobo-time">
                       ${ todo.created_time }
                   </div>
                   <div class="todo-update left clear-fix hide">
                       <input type="text" class="todo-input-update">
                       <button class="todo-update-commit">提交</button>
                   </div>
               </div>
               `
    return t
}
var log = function(){
    console.log(arguments)
}
$(document).ready(function(){

    // 添加 todo
    $('.todo-button-add').on('click', function(){
        var inputDiv = $(this).closest('.todo-new')
        var input = inputDiv.find('.todo-input-add')
        var task = input.val()
        var addDiv = inputDiv.closest('.container').find('.todo-main')
        var form = {
            task: task
        }
        var response = function(r){
            if(r.success) {
                var todo = r.data
                addDiv.prepend(addTemplate(todo))
                alertify.success(r.message)
                input.val('')
            }else {
                alertify.error(r.message)
            }
        }
        api.todoAdd(form, response)
    })
    // 删除 todo
    $('.todo-main').on('click', '.todo-button-delete', function(){
        var todo = $(this).closest('.todo-cell')
        var todoId = todo.data('id')
        var url = '/api/delete/' + todoId
        log('todoid', todoId)
        var response = function(r){
            if(r.success) {
                todo.slideUp()
                alertify.success(r.message)
            }else {
                alertify.error(r.message)
            }
        }
        api.todoDelete(url, response)
    })
    // 显示更新todo 界面
    $('.todo-main').on('click', '.todo-button-update', function(){
        var todo = $(this).closest('.todo-cell')
        var update = todo.find('.todo-update')
        update.slideToggle()
    })
    // 更新 todo
    $('.todo-main').on('click', '.todo-update-commit', function(){
        var todo = $(this).closest('.todo-cell')
        var todoId = todo.data('id')
        var input = todo.find('.todo-input-update')
        var content = input.val()
        var update = todo.find('.todo-update')
        var div = todo.find('.todo-content')
        var url = '/api/update/' + todoId
        var form = {
            task: content
        }
        var response = function(r){
            if(r.success) {
                var task = r.data.task
                div.text(task)
                update.slideUp()
                input.val('')
                alertify.success(r.message)
            }else {
                alertify.error(r.message)
            }
        }
        api.todoUpdate(url, form, response)
    })
})