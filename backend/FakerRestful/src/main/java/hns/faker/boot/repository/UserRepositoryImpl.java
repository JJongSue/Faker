package hns.faker.boot.repository;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import hns.faker.boot.dto.UserVo;

@Repository("UserRepositoryImpl")
public class UserRepositoryImpl implements UserRepository{
	@Autowired
	SqlSession session;

	@Override
	public int insertUser(UserVo user) {
		// TODO Auto-generated method stub
		return session.insert("ssafy.user.insert", user);
		
	}

	@Override
	public int updateUser(UserVo user) {
		// TODO Auto-generated method stub
		return session.update("ssafy.user.update", user);
	}

	@Override
	public int deleteUser(int user_id) {
		// TODO Auto-generated method stub
		return session.delete("ssafy.user.delete", user_id);
	}

	@Override
	public UserVo selectUser(int user_id) {
		// TODO Auto-generated method stub
		return session.selectOne("ssafy.user.selectOne", user_id);
	}

	@Override
	public UserVo login(String username) {
		// TODO Auto-generated method stub
		return session.selectOne("ssafy.user.login",username);
	}
	
	
}
