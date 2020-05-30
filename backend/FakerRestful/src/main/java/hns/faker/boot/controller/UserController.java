package hns.faker.boot.controller;

import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import hns.faker.boot.dto.UserVo;
import hns.faker.boot.service.UserService;
import hns.faker.boot.util.JwtTokenProvider;

@CrossOrigin(origins = { "*" }, maxAge = 6000)
@RestController
@RequestMapping("api/user")
public class UserController {
	@Autowired
	UserService userService;
	@Autowired
	JwtTokenProvider jwtTokenProvider;

	// 로그인
	@PostMapping("/login")
	public ResponseEntity<Map<String, Object>> login(@RequestBody UserVo uservo) {
		ResponseEntity<Map<String, Object>> resEntity = null;
		try {
			Map<String, Object> msg = new HashMap<String, Object>();
			UserVo user = userService.loginUser(uservo.getUsername());
			if (user != null) {
				String inputpw = userService.passwordEncryption(uservo.getPassword());
				String pw = user.getPassword();
				if (inputpw.equals(pw)) {
					String token= jwtTokenProvider.createToken(user.getUser_id()+"", user.getUsername());
					msg.put("token", token);
					msg.put("resMsg", "로그인 성공");
				} else {
					msg.put("resMsg", "로그인 실패");
				}
			} else {

			}

			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		} catch (RuntimeException e) {
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("resMsg", "로그인 실패");
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		}
		return resEntity;

	}

	@GetMapping(path = "/select/{user_id}")
	private ResponseEntity<Map<String, Object>> selectUser(@PathVariable int user_id) {
		ResponseEntity<Map<String, Object>> resEntity = null;
		try {
			System.out.println(user_id);
			UserVo user = userService.selectUser(user_id);
			System.out.println(user.toString());
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("code", "00");
			msg.put("data", user);
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);

		} catch (RuntimeException e) {
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("code", "01");
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		}
		return resEntity;
	}

	// 회원가입
	@PostMapping(path = "/join")
	private ResponseEntity<Map<String, Object>> insertUser(@RequestBody UserVo uservo) {
		ResponseEntity<Map<String, Object>> resEntity = null;
		try {
			System.out.println(uservo.toString());
			int res = userService.insertUser(uservo);
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("resMsg", "회원 등록성공");
//			msg.put("resValue", uservo.getUser_id());
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		} catch (RuntimeException e) {
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("resMsg", "회원 등록실패 - RE");
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		}
		return resEntity;
	}

	@PutMapping(path = "update")
	private ResponseEntity<Map<String, Object>> updateUser(@RequestBody UserVo uservo) {
		ResponseEntity<Map<String, Object>> resEntity = null;
		try {

			int res = userService.updateUser(uservo);
			System.out.println(res);
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("code", "00");
			msg.put("resValue", uservo.getUser_id());
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		} catch (RuntimeException e) {
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("resMsg", "업데이트 실패 - RE");
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		}
		return resEntity;
	}

	@DeleteMapping(path = "delete/{user_id}")
	private ResponseEntity<Map<String, Object>> deleteUser(@PathVariable int user_id) {
		ResponseEntity<Map<String, Object>> resEntity = null;
		try {

			int res = userService.deleteUser(user_id);
			System.out.println(res);
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("code", "00");
//			msg.put("resValue", uservo.getUser_id());
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		} catch (RuntimeException e) {
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("resMsg", "업데이트 실패 - RE");
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		}
		return resEntity;
	}
}
