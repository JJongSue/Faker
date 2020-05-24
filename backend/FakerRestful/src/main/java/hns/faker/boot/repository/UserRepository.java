package hns.faker.boot.repository;

import hns.faker.boot.dto.UserVo;

public interface UserRepository {
	public int insertUser(UserVo user);
	public int updateUser(UserVo user);
	public int deleteUser(int user_id);
	public UserVo selectUser(int user_id);
	public UserVo login( UserVo user);
}
