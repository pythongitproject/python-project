
$("#hot").click(function () {
        $("#single").removeClass('active');
        $(this).addClass('active');
        window.location.href = '/index';
    });

$("#release").click(function () {
    var getname = $.cookie('telno')
    if(getname!=null){
         $('#pub').modal('show');
    }else {
        layer.msg('登录才能发布帖子哦', {
          time: 0 //不自动关闭
          ,btn: ['登录', '再想想']
          ,yes: function(index){
            layer.close(index);
            window.location.href = "/login";
          }
        });
    }
});

$("#sb").click(function () {
            var flag = true;
            if($("#title").val().trim()==''){
                alert('标题不能为空哦');
                flag = false;
                //return false;
            }else {
                if($("#content").val().trim()==''){
                    alert('内容不能为空哦');
                    flag = false;
                    //return false;
                }else {
                    if(flag){
                         $.ajax({
                            url : "/release",
                            type :"post",
                            data:{
                                'title':$("#title").val().trim(),
                                'content':$("#content").val().trim()
                            },
                             beforeSend :function () {
                                $("#sb").val("提交中...");
                             },
                            success:function (returndata) {
                                dic = JSON.parse(returndata)
                                if(dic.status){
                                    $('#pub').modal("hide");
                                    window.location.href = "/index";
                                }else {
                                    alert("发布失败，请重试");
                                }
                            }
                        });
                    }

                }
            }
});

 $("#hot").click(function () {
        window.location.href = '/index';
    });