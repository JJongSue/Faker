package hns.faker.boot.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import hns.faker.boot.dto.UserVo;
import hns.faker.boot.repository.UserRepository;

@Service("UserServiceImpl")
public class UserServiceImpl implements UserService{
	@Autowired
	UserRepository repo;

	@Override
	public int userInsert(UserVo user) {
		// TODO Auto-generated method stub
		return repo.userInsert(user);
	}
	
	
}
