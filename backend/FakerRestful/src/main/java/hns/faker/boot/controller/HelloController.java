package hns.faker.boot.controller;

import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import hns.faker.boot.dto.UserVo;
import hns.faker.boot.service.UserService;

@CrossOrigin(origins = {"*"}, maxAge = 6000)
@RestController
public class HelloController {
	
	@Autowired
	UserService userService;
	
	@GetMapping(path="/hello")
	public String HelloSpringWorld() {
		return "Hello Spring World";
	}
	
	@PostMapping(path="/user")
	private ResponseEntity<Map<String, Object>> memInsert(@RequestBody UserVo uservo) {
		ResponseEntity<Map<String, Object>> resEntity = null;
		try {
			System.out.println(uservo.toString());
			userService.userInsert(uservo);
			System.out.println("되는겨");
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("resMsg", "회원 등록성공");
			msg.put("resValue", uservo.getUser_id());
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		} catch (RuntimeException e) {
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("resMsg", "회원 등록실패 - RE");
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		}
		return resEntity;
	}

	
	
}
