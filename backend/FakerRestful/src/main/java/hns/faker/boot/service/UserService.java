package hns.faker.boot.service;

import hns.faker.boot.dto.UserVo;

public interface UserService {
	public int insertUser(UserVo user);
	public int updateUser(UserVo user);
	public int deleteUser(int user_id);
	public UserVo selectUser(int user_id);
}
