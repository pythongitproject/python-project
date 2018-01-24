
$(".icon-thumbs-up").click(function () {
    var getname = $.cookie('telno');
    var counts =$(this).attr("count");
    var aa = $(this);
    var isClick = false;
    if(getname!=null){
        $.ajax({
            type : 'post',
            url : '/click',
            data : {
                'newsid' : $(this).attr("addd"),
                'click_count': counts
            },
            success: function (returndata) {
                dd = JSON.parse(returndata);
                if(dd.status){
                        isClick = true;
                        if(isClick){
                            aa.attr('count',parseInt(counts) + 1);
                            aa.html(parseInt(counts) + 1);
                        }
                }else {
                    isClick = false;
                    switch (dd.typeid){
						case -1:
						     layer.msg('登录才能点赞哦', {
								  time: 0 //不自动关闭
								  ,btn: ['登录', '算了']
								  ,yes: function(index){
									layer.close(index);
									window.location.href = "/login";
								  }
								});
						     break;
                        case -3:
                             alert(dd.msg);
                            break;
                        case -4:
                             alert(dd.msg);
                            break;
                        default:
                            alert('what happen???');
                            break;
                    }
                }
            }
        });
    }else {
        layer.msg('登录才能点赞哦', {
          time: 0 //不自动关闭
          ,btn: ['登录', '算了']
          ,yes: function(index){
            layer.close(index);
            window.location.href = "/login";
          }
        });
    }

});

$("#single_index").click(function () {
        var getname = $.cookie('telno');
        if(getname!=null){
            window.location.href = '/single_index';
        }else {
            layer.msg('登录查看个人Post', {
              time: 0 //不自动关闭
              ,btn: ['登录', '偏不']
              ,yes: function(index){
                layer.close(index);
                window.location.href = "/login";
              }
            });
        }


    });

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