package hns.faker.boot.dto;

public class ContentsVo {
	private int content_id;
	private int user_id;
	private String content_type;
	private String content_src;
	public ContentsVo(int content_id, int user_id, String content_type, String content_src) {
		super();
		this.content_id = content_id;
		this.user_id = user_id;
		this.content_type = content_type;
		this.content_src = content_src;
	}
		
	//insert시 user_id하고 type, src만 받고 insert하는 문 
	public ContentsVo(int user_id, String content_type, String content_src) {
		super();
		this.user_id = user_id;
		this.content_type = content_type;
		this.content_src = content_src;
	}

	public int getContent_id() {
		return content_id;
	}
	public void setContent_id(int content_id) {
		this.content_id = content_id;
	}
	public int getUser_id() {
		return user_id;
	}
	public void setUser_id(int user_id) {
		this.user_id = user_id;
	}
	public String getContent_type() {
		return content_type;
	}
	public void setContent_type(String content_type) {
		this.content_type = content_type;
	}
	public String getContent_src() {
		return content_src;
	}
	public void setContent_src(String content_src) {
		this.content_src = content_src;
	}
	@Override
	public String toString() {
		return "ContentVo [content_id=" + content_id + ", user_id=" + user_id + ", content_type=" + content_type
				+ ", content_src=" + content_src + "]";
	}
	
}
