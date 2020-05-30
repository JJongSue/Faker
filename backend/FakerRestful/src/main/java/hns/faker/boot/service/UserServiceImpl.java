package hns.faker.boot.service;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import hns.faker.boot.dto.UserVo;
import hns.faker.boot.repository.UserRepository;

@Service("UserServiceImpl")
public class UserServiceImpl implements UserService {
	@Autowired
	UserRepository repo;

	@Override
	public int insertUser(UserVo user) {
		user.setPassword(passwordEncryption(user.getPassword()));
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

	@Override
	public UserVo loginUser(String username) {
			return  repo.login(username);
	}

	@Override
	public String passwordEncryption(String rowPassword) {
		String SHA = "";
		try {
			MessageDigest sh = MessageDigest.getInstance("SHA-256");
			sh.update(rowPassword.getBytes());
			byte byteData[] = sh.digest();
			StringBuffer sb = new StringBuffer();
			for (int i = 0; i < byteData.length; i++) {
				sb.append(Integer.toString((byteData[i] & 0xff) + 0x100, 16).substring(1));
			}
			SHA = sb.toString();

		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
			SHA = null;
		}
		return SHA;
	}

}
