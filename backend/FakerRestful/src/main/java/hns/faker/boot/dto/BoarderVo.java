package hns.faker.boot.dto;

public class BoarderVo {
	private int boarder_id; 
	private int contents_id; 
	private int view_cnt; 
	private String boarder_title; 
	private String boarder_description;
	
	
	public int getBoarder_id() {
		return boarder_id;
	}
	public void setBoarder_id(int boarder_id) {
		this.boarder_id = boarder_id;
	}
	public int getContents_id() {
		return contents_id;
	}
	public void setContents_id(int contents_id) {
		this.contents_id = contents_id;
	}
	public int getView_cnt() {
		return view_cnt;
	}
	public void setView_cnt(int view_cnt) {
		this.view_cnt = view_cnt;
	}
	public String getBoarder_title() {
		return boarder_title;
	}
	public void setBoarder_title(String boarder_title) {
		this.boarder_title = boarder_title;
	}
	public String getBoarder_description() {
		return boarder_description;
	}
	public void setBoarder_description(String boarder_description) {
		this.boarder_description = boarder_description;
	} 
	
	
}

