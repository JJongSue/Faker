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
	public int userInsert(UserVo user) {
		// TODO Auto-generated method stub
		return session.insert("ssafy.user.insert", user);
		
	}
	
}
