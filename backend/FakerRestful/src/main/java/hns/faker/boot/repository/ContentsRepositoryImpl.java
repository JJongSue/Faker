package hns.faker.boot.repository;

import org.apache.ibatis.session.SqlSession;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import hns.faker.boot.dto.ContentsVo;

@Repository("ContentsRepositofyImpl")
public class ContentsRepositoryImpl implements ContentsRepository{
	@Autowired
	SqlSession session;

	@Override
	public int insertContents(ContentsVo contents) {
		return session.insert("ssafy.contents.insert", contents);
	}

	@Override
	public int updateContents(ContentsVo contents) {
		return session.update("ssafy.contents.update", contents);
	}

	@Override
	public int deleteContents(int contents_id) {
		return session.delete("ssafy.contents.delete", contents_id);
	}

	@Override
	public ContentsVo selectContens(int contents_id) {
		return session.selectOne("ssafy.contents.selectOne", contents_id);
	}

}
