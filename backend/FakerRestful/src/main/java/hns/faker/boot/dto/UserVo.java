package hns.faker.boot.dto;

public class UserVo {
	private int user_id;
	private String username;
	private String password;
	private String gender;
	private int age;
	
	// user_id를 제외한 나머지를 받고 만들어주는 생성자
	public UserVo(String username, String password, String gender, int age) {
		super();
		this.username = username;
		this.password = password;
		this.gender = gender;
		this.age = age;
	}
	public UserVo(int user_id, String username, String password, String gender, int age) {
		super();
		this.user_id = user_id;
		this.username = username;
		this.password = password;
		this.gender = gender;
		this.age = age;
	}
	
	public UserVo() {
		super();
		// TODO Auto-generated constructor stub
	}
	public int getUser_id() {
		return user_id;
	}
	public void setUser_id(int user_id) {
		this.user_id = user_id;
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getGender() {
		return gender;
	}
	public void setGender(String gender) {
		this.gender = gender;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	@Override
	public String toString() {
		return "UserVo [user_id=" + user_id + ", username=" + username + ", password=" + password + ", gender=" + gender
				+ ", age=" + age + "]";
	}
	
	
	
	
	
}
