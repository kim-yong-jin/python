<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<link href="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
//해당 불린 값들이 정규식에 맞게 입력되면 true로 변경
//정규식과 다를때는 false

	idPass = false; //아이디 인증값
	pwPass = false; //비밀번호 인증값
	pw2Pass = false; //비밀번호 비교 인증값
	emailpass = false //이메일 인증값
	mailPass = false; //이메일 인증번호 인증 값
	$(function() {
		//아이디 정규식
		$("#id").on("keyup", function() {
			idval = $("#id").val().trim();

			regid = /^[a-z][a-zA-Z0-9]{3,11}$/;

			if(!regid.test(idval)){
				regfail(this,"올바른 형식이 아닙니다");
				idPass= false;
				
			}else{
				regpass(this);
				idPass= true;
				
			}
		});
		
		
		//비밀번호
		$("#pwd").on("keyup",function(){
			passval = $(this).val().trim();
			regpwd = /^.*(?=.{6,20})(?=.*[0-9])(?=.*[a-zA-Z]).*$/;
			
			if(!regpwd.test(passval)){
				regfail(this,"영문 + 숫자 20자리 이내로 입력 해주세요");
				pwPass= false;
			}
			else if(regpwd.test(passval)){
				regfail(this,"사용가능한 비밀번호 입니다");
				pwPass= true;
				pwdPass1 = true;
			}
			else{
				regpass(this);
			}
		});
		
		//비밀번호 비교
		$("#pwd2").on("keyup",function(){
			pass2val = $(this).val().trim();
			passval = $("#pwd").val().trim();
			
			if(pass2val == passval) {
				regpass(this,"비밀번호가 일치 합니다");
				pw2Pass = true;
				
				
			}
			else{ 
				regfail(this,"일치하지 않습니다");
				pw2Pass= false;
			
			}
		});
		
		//이메일 
		$('#email').on('keyup', function() {
			emailval = $(this).val().trim();
			regemail = /^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/;

			if (!(regemail.test(emailval))) {
				regfail(this , "올바른 형식이 아닙니다.");

			} else {
				regpass(this,"올바른 형식 입니다.");
				emailpass = true;
			}
		});
		
		//인증번호 전송
		$("#mailcheck").on("click",function(){
			email = $("#email").val();
			
			$.ajax({
				url : '<%=request.getContextPath()%>/common/SendEmailServlet',
				type : 'get',
				data : {"email" : email},
				success : function(res) {
					alert("전송완료");					
				},
				error : function (req){
					alert("req : " + req.status);
				},
				dataType : 'html'
			});
		});
		
		//일반회원 인증번호입력
		$("#mailcheck2").on('click',function(){
			mailinput = $("#mailinput").val();
			
			
			$.ajax({
				url : '<%=request.getContextPath()%>/common/GetEmailServlet',
				type : "post",
				data : {"mailinput" : mailinput},
				success : function(res) {
					if(mailPass == true){
						alert("이미 인증하셨습니다.");
						return;
					}
					alert(res);
					
					if(res=="인증완료"){
						$("#mailinput").attr("readonly",true);
						mailPass= true;
						mailPassS = true;
					}else{
						mailPass= false;
						mailPassS = false;
					}
					
					
				},
				error : function (req){
					alert("req : " + req.status);
				},
				dataType : 'html'
			});
		})
		
		//아이디 중복검사
		$("#idCheck").on("click", function(){
			
			id = $("#id").val();
		
			$.ajax({
				
				url : "<%=request.getContextPath()%>/common/IdCheck.do",
				data : { "id" : id },
				type : "post",
				success : function (res) {
					if(res.sw == "false" || id == ""){
						alert("중복된 아이디 또는 공백 입니다.");
					}
					else if(res.sw == "true"){
						idPass2 = true;
						alert("사용가능한 아이디입니다.")
					}
				},
				dataType : "json"
				
			});
			
			
		});
		
		
		//회원가입 
		//맨위에 전역으로 선언된 모든 불린 값들이 true일때 클릭 이벤트 발생
		$("#chk").on("click",function(){
			if(idPass == true && pwPass == true && pw2Pass == true && emailpass == true && mailPass == true){
			
				$('#registform').submit();
			}else{
				alert("누락된 항목 및 입력을 바르게 해주세요")
			}
		})
		
		$("#back").on("click",function(){
			location.href="<%=request.getContextPath()%>/common/loginForm.do";
		})
		
	
		function regpass(target, text) {

			
			$(target).parents(".form-group").find('.msg').empty();
			
			
			// 실패메세지 지우기
			$(target).parents(".form-group").find('.msg').html(text)
           									.css('color', 'red').addClass('text-center text-danger');;
		}

		// 정규식 실패메소드
		function regfail(target, text) {
			// 이미지 지우기
			$(target).parents(".form-group").find('.msg').empty();
		
			// 실패 메세지 출력
			$(target).parents(".form-group").find('.msg').html(text)
			                                .css('color', 'red').addClass('text-center text-danger');
		}
	})
</script>
<style type="text/css">
		button {
		  display: inline-block;
		  padding: 12px 24px;
		  background: rgb(220,220,220);
		  font-weight: bold;
		  color: rgb(120,120,120);
		  border: none;
		  outline: none;
		  border-radius: 50px;
		  cursor: pointer;
		  transition: ease .3s;
		  margin-left: 10px;
		}
		
		button:hover .button{		
		  background: #8BC34A;
		  color: #ffffff;
		}
	</style>


</head>
<body>
	<form action="<%=request.getContextPath() %>/member/registForm.do" method="post" id ="registform">
		
			<div class="row justify-content-center">
               <div class="col-md-8">
                   <div class="card">
                       <div class="card-header">Register</div>
                       <div class="card-body">
                               <div class="form-group">
                                   <label for="name" class="cols-sm-2 control-label">Your ID</label>
                                   <div class="cols-sm-10">
                                       <div class="input-group">
                                           <span class="input-group-addon"><i class="fa fa-user fa" aria-hidden="true"></i></span>
                                           <input type="text" class="form-control" name="id" id="id" placeholder="Enter your id" />
                                           <button type ="button" id ="idCheck" class="btn btn-outline-secondary logout">중복확인</button>
                                       </div>
                                        <div class = "msg" id = "namemsg"></div>
                                   </div>
                               </div>
                               
                               <div class="form-group">
                                   <label for="password" class="cols-sm-2 control-label">Password</label>
                                   <div class="cols-sm-10">
                                       <div class="input-group">
                                           <span class="input-group-addon"><i class="fa fa-lock fa-lg" aria-hidden="true"></i></span>
                                           <input type="password" class="form-control" name="pwd" id="pwd" placeholder="Enter your Password" />
                                       </div>
                                       <div class = "msg" id = "namemsg"></div>
                                   </div>
                               </div>
                               
                                <div class="form-group">
                                   <label for="password" class="cols-sm-2 control-label">Password comparison</label>
                                   <div class="cols-sm-10">
                                       <div class="input-group">
                                           <span class="input-group-addon"><i class="fa fa-lock fa-lg" aria-hidden="true"></i></span>
                                           <input type="password" class="form-control" name="pwd2" id="pwd2" placeholder="Enter your Password" />                 
                                       </div>
                                  	<div class = "msg" id = "namemsg"></div>
                                   </div>
                               </div>
                               
                               
                                <div class="form-group">
                                   <label for="username" class="cols-sm-2 control-label">Username</label>
                                   <div class="cols-sm-10">
                                       <div class="input-group">
                                           <span class="input-group-addon"><i class="fa fa-users fa" aria-hidden="true"></i></span>
                                           <input type="text" class="form-control" name="name" id="name" placeholder="Enter your Username" />
                                       </div>
                                   </div>
                               </div>
                               
                                <div class="form-group">
                                   <label for="email" class="cols-sm-2 control-label">Your Phone</label>
                                   <div class="cols-sm-10">
                                       <div class="input-group">
                                           <span class="input-group-addon"><i class="fa fa-envelope fa" aria-hidden="true"></i></span>
                                           <input type="text" class="form-control" name="phone" id="phone" placeholder="Enter your Email" />
                                       </div>
                                   </div>
                               </div>
                               
                               <div class="form-group">
                                   <label for="email" class="cols-sm-2 control-label">Your Email</label>
                                   <div class="cols-sm-10">
                                       <div class="input-group">
                                           <span class="input-group-addon"><i class="fa fa-envelope fa" aria-hidden="true"></i></span>
                                           <input type="text" class="form-control" name="email" id="email" placeholder="Enter your Email" />
                                           <button type ="button" id ="mailcheck"  class="btn btn-outline-secondary logout">인증번호 전송</button>
                                       </div>
                                       
                                       <div class = "msg" id = "namemsg"></div>
                                       
                                   </div>
                               </div>
                              
                               <div class="form-group">
                                   <label for="email" class="cols-sm-2 control-label">Your Email certification</label>
                                   <div class="cols-sm-10">
                                       <div class="input-group">
                                           <span class="input-group-addon"><i class="fa fa-envelope fa" aria-hidden="true"></i></span>
                                           <input type="text" class="form-control" name="mailinput" id = "mailinput" placeholder="Enter your Email" />
                                           <button type ="button" 
                                           class="btn btn-outline-secondary logout"  id = "mailcheck2">
                                        	인증확인</button>
                                       </div>
                                       
                                       <div class = "msg" id = "namemsg"></div>
                                       
                                   </div>
                               </div>
                              
                            
                               <div class="form-group ">
                                   <button type="button" id ="chk" class="btn btn-primary btn-lg btn-block login-button">회원가입</button>
                               </div>
                             	<div class="form-group ">
                                   <button type="button" id = "back" class="btn btn-primary btn-lg btn-block login-button">뒤로가기</button>
                               </div>
                           
                       </div>

                   </div>
               </div>
           </div>
		</div>
	</form>
</body>
</html>