package hns.faker.boot.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import hns.faker.boot.dto.ContentsVo;
import hns.faker.boot.repository.ContentsRepository;

@Service("ContentsServiceImpl")
public class ContentsServiceImpl implements ContentsService{

	@Autowired
	ContentsRepository repo;
	
	@Override
	public int insertContents(ContentsVo contents) {
		return repo.insertContents(contents);
	}

	@Override
	public int updateContents(ContentsVo contents) {
		// TODO Auto-generated method stub
		return repo.updateContents(contents);
	}

	@Override
	public int deleteContents(int contents_id) {
		// TODO Auto-generated method stub
		// user_id가 같은지 확인 
		return repo.deleteContents(contents_id);
	}

	@Override
	public ContentsVo selectContents(int contents_id) {
		return repo.selectContens(contents_id);
	}

}
