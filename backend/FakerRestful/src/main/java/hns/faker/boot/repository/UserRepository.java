package hns.faker.boot.repository;

import hns.faker.boot.dto.UserVo;

public interface UserRepository {
	public int userInsert(UserVo user);
}
