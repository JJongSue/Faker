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
	public int insertUser(UserVo user) {
		// TODO Auto-generated method stub
		return repo.insertUser(user);
	}

	@Override
	public int updateUser(UserVo user) {
		// TODO Auto-generated method stub
		return repo.updateUser(user);
	}

	@Override
	public int deleteUser(int user_id) {
		// TODO Auto-generated method stub
		return repo.deleteUser(user_id);
	}

	@Override
	public UserVo selectUser(int user_id) {
		// TODO Auto-generated method stub
		return repo.selectUser(user_id);
	}
	
	
}
