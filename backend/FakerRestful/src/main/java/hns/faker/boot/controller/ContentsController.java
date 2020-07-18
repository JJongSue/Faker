package hns.faker.boot.controller;

import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import hns.faker.boot.dto.ContentsVo;
import hns.faker.boot.dto.UserVo;
import hns.faker.boot.service.ContentsService;

@CrossOrigin(origins = {"*"}, maxAge = 6000)
@RestController
@RequestMapping("api/contents")
public class ContentsController {
	@Autowired
	ContentsService contentsService; 
	
	//등록
	@PostMapping(path="/registe")
	private ResponseEntity<Map<String, Object>> insertContents(@RequestBody ContentsVo contentvo){
		ResponseEntity<Map<String, Object>> resEntity = null ; 
		try {
			int res = contentsService.insertContents(contentvo);
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("resMsg", "컨텐츠 등록 성공");
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		}catch(RuntimeException e) {
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("resMsg", "컨텐츠 등록 실패");
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		}
		return resEntity; 
	}
	//수정
	@PutMapping(path="/update")
	private ResponseEntity<Map<String, Object>> updateContents(@RequestBody ContentsVo contentvo){
		ResponseEntity<Map<String, Object>> resEntity = null ; 
		try {
			int res = contentsService.updateContents(contentvo);
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("resMsg", res+"개 컨텐츠 업데이트 성공");
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		}catch(RuntimeException e) {
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("resMsg", "컨텐츠 업데이트 실패");
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		}
		return resEntity; 
	}
	
	//삭제
	@DeleteMapping(path="/delete/{contents_id}")
	private ResponseEntity<Map<String, Object>> deleteContents(@PathVariable int contents_id){
		ResponseEntity<Map<String, Object>> resEntity = null ; 
		try {
			int res = contentsService.deleteContents(contents_id);
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("resMsg", res+"개 컨텐츠 삭제 성공");
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		}catch(RuntimeException e) {
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("resMsg", "컨텐츠 삭제 실패");
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		}
		return resEntity; 
	}
	//조회 
	@GetMapping(path = "/select/{contents_id}")
	private ResponseEntity<Map<String, Object>> selectUser(@PathVariable int contents_id) {
		ResponseEntity<Map<String, Object>> resEntity = null;
		try {
			ContentsVo contents = contentsService.selectContents(contents_id);
			System.out.println(contents.toString());
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("code", "00");
			msg.put("data", contents);
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);

		} catch (RuntimeException e) {
			Map<String, Object> msg = new HashMap<String, Object>();
			msg.put("code", "01");
			resEntity = new ResponseEntity<Map<String, Object>>(msg, HttpStatus.OK);
		}
		return resEntity;
	}
}
