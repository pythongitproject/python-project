
    function isPoneAvailable(str) {
          var myreg=/^[1][3,4,5,,6,7,8,9][0-9]{9}$/;
          if (!myreg.test(str)) {
              return true;
          } else {
              return false;
          }
      }
    //刷新验证码
    function Changecode() {
            $("#getcode").attr("src","/check_code?flag="+Math.random());
    }
    $("#sb").on("click",function () {
        var flag = true;
            if($("#telno").val().trim()==''){
                flag=false;
                $("#terror").text('手机号码不能为空哦');
                $("#perror").text('');
                 $("#cerror").text('');
            }else {
                $("#terror").text('');
                if ($("#telno").val().trim().length<11 || isPoneAvailable($("#telno").val().trim())){
                    flag=false;
                    $("#terror").text('请输入11位的手机号码哦');
                    $("#perror").text('');
                    $("#cerror").text('');
                }else {
                    if($("#pwd").val().trim()==''){
                        flag=false;
                        $("#perror").text('登录密码不能为空哦');
                         $("#cerror").text('');
                         $("#terror").text('');
                    }else {
                        $("#perror").text('');
                        if ($("#code").val().trim()==''){
                            flag=false;
                            $("#cerror").text('验证码不能为空哦');
                            $("#perror").text('');
                            $("#terror").text('');
                        }else {
                            $("#cerror").text('');
                             if(flag){
                            $.post("/login",
                            {"telno":$("#telno").val().trim(),"password":$("#pwd").val().trim(),"code":$("#code").val().trim()},
                            function (callback) {
                               var data = callback;
                               var ret_dict = JSON.parse(data);
                               console.log(ret_dict)
                               if(ret_dict.status){
                                   window.location.href = "/index";
                               }else {
                                   var id = ret_dict.typeid;
                                   switch (id){
                                       case -1 :
                                           $("#telno").val("");
                                           $("#pwd").val("");
                                           $("#code").val("");
                                           Changecode();
                                           $("#terror").text(ret_dict.msg);
                                           break;
                                       case -2 :
                                            $("#cerror").text(ret_dict.msg);
                                            $("#code").val("");
                                            Changecode();
                                           break;
                                       case -3 :
                                           $("#terror").text(ret_dict.msg);
                                           $("#telno").val("");
                                           $("#pwd").val("");
                                           $("#code").val("");
                                           Changecode();
                                           break;
                                       default:
                                           alert('网络君闹情绪了,请重试！')
                                           break;
                                   }
                               }
                            });
                        }
                        }
                    }
                }
            }
    });


